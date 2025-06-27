import subprocess

def get_changed_folders():
    result = subprocess.run(
        ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
        capture_output=True, text=True
    )
    changed_files = result.stdout.strip().split('\n')
    changed_services = set()
    for file in changed_files:
        if file.startswith('user-service/'):
            changed_services.add('user-service')
        elif file.startswith('product-service/'):
            changed_services.add('product-service')
    print(','.join(changed_services))

if __name__ == '__main__':
    get_changed_folders()
