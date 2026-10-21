#!/usr/bin/env python3
"""Reproduce native packaging on Debian 13 without installing system packages.

Downloads pinned official Otzaria and Debian runtime packages to work/. The local
libmount selector avoids the official bundle's older copy; no system file changes.
--open launches the existing .otzplugin in an isolated native test profile afterward.
This check does not certify source scholarship or successful indexed-book opening.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import select
import shutil
import subprocess
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent
PACKAGES = [
    ('otzaria', 'https://github.com/Otzaria/otzaria/releases/download/0.9.98%2B801/otzaria-0.9.98%2B99800-linux.deb', 'cb2cef903b165f1e38a557a23bcc2819ae1af3a05b1e206d416dc62e61880d7f'),
    ('harfbuzz-icu', 'https://deb.debian.org/debian/pool/main/h/harfbuzz/libharfbuzz-icu0_10.2.0-1+deb13u1_amd64.deb', '0b45d951629e98673c0da73b2bcd0886a467d833bb3b7499892a168f247165d2'),
    ('gles', 'https://deb.debian.org/debian/pool/main/libg/libglvnd/libgles2_1.7.0-1+b2_amd64.deb', 'e12c18aa77939d122ee1dea520ba0440b97dc19200b7396e03dff03a3ece74c1'),
    ('xvfb', 'https://deb.debian.org/debian/pool/main/x/xorg-server/xvfb_21.1.16-1.3+deb13u4_amd64.deb', '893d87bf159b6de077a929fc796a73c39f837d45310b2076e3eeebebb80552b6'),
]

def payload(path):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, path
        return {name: hashlib.sha256(archive.read(name)).hexdigest() for name in archive.namelist()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--open', action='store_true', help='Open the current package in an isolated GUI profile after packing')
    args = parser.parse_args()
    work = ROOT / 'work/native-validation'
    work.mkdir(parents=True, exist_ok=True)
    for name, url, digest in PACKAGES:
        package = work / (name + '.deb')
        if not package.exists() or hashlib.sha256(package.read_bytes()).hexdigest() != digest:
            temporary = package.with_suffix('.download')
            with urllib.request.urlopen(url, timeout=40) as response, temporary.open('wb') as output:
                shutil.copyfileobj(response, output)
            assert hashlib.sha256(temporary.read_bytes()).hexdigest() == digest, ('download checksum', name)
            temporary.replace(package)
        subprocess.run(['dpkg-deb', '-x', str(package), str(work / ('app' if name == 'otzaria' else 'deps'))], check=True)
    app = work / 'app/opt/otzaria'
    local_lib = work / 'lib'
    local_lib.mkdir(exist_ok=True)
    system_mount = Path('/usr/lib/x86_64-linux-gnu/libmount.so.1')
    assert system_mount.exists(), 'This runtime recipe requires Debian 13 amd64 with system libmount'
    mount = local_lib / 'libmount.so.1'
    mount.unlink(missing_ok=True)
    mount.symlink_to(system_mount)
    env = dict(os.environ)
    for kind, variable in [('config','XDG_CONFIG_HOME'),('data','XDG_DATA_HOME'),('cache','XDG_CACHE_HOME')]:
        directory = work / 'profile' / kind
        directory.mkdir(parents=True, exist_ok=True)
        env[variable] = str(directory)
    documents = work / 'profile/documents'
    documents.mkdir(exist_ok=True)
    (work / 'profile/config/user-dirs.dirs').write_text(f'XDG_DOCUMENTS_DIR="{documents}"\nXDG_DOWNLOAD_DIR="{documents}"\n')
    env['LD_LIBRARY_PATH'] = ':'.join(map(str, [local_lib, work / 'deps/usr/lib/x86_64-linux-gnu', app / 'lib']))
    env['WEBKIT_EXEC_PATH'] = env['WEBKIT_INJECTED_BUNDLE_PATH'] = str(app / 'lib')
    with (work / 'display.log').open('w') as display_log:
        display = subprocess.Popen([str(work / 'deps/usr/bin/Xvfb'), '-displayfd', '1', '-screen', '0', '1280x900x24', '-nolisten', 'tcp'], stdout=subprocess.PIPE, stderr=display_log)
        try:
            assert select.select([display.stdout], [], [], 10)[0], 'Virtual display did not become ready; see display.log'
            number = display.stdout.readline().decode().strip()
            assert number.isdigit(), ('virtual display startup', number)
            env['DISPLAY'] = ':' + number
            output = work / 'Mevoot-Shas-0.13.10.otzplugin'
            command = [str(app / 'otzaria.bin'), 'pack-plugin', str(ROOT / 'plugin'), '--output', str(output), '--force']
            result = subprocess.run(command, cwd=work, env=env, capture_output=True, text=True, timeout=60)
            (work / 'packager.log').write_text(result.stdout + result.stderr)
            assert result.returncode == 0, ('native packager failed', result.returncode, result.stderr)
            actual = payload(output)
            assert actual == payload(ROOT / 'dist/Mevoot-Shas-0.13.10.otzplugin'), 'Native package payload differs from tested Python package'
            receipt = {'official_release':'0.9.98+801', 'plugin_version':'0.13.10', 'native_packager_exit':result.returncode, 'package_sha256':hashlib.sha256(output.read_bytes()).hexdigest(), 'package_file_hashes':actual, 'same_payload_as_tested_package':True, 'runtime_package_sha256':{name:digest for name,_,digest in PACKAGES}, 'limits':'Native packaging only. --open permits manual GUI installation/reading checks; indexed reader opening and scholarly approval are separate.'}
            (work / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
            print('PASS native Otzaria packager: 10 files, CRC valid, payload identical to tested 0.13.10 package.')
            if args.open:
                print('Opening isolated native test profile on display '+env['DISPLAY']+'. Close Otzaria to finish; no release or publication occurs.', flush=True)
                subprocess.run(['dbus-run-session', '--', str(app / 'otzaria.bin'), str(ROOT / 'dist/Mevoot-Shas-0.13.10.otzplugin')], cwd=work, env=env, check=True)
        finally:
            display.terminate()
            display.wait(timeout=10)

if __name__ == '__main__':
    main()
