import re, os
for root, dirs, files in os.walk('/app/bazarr/bin/frontend/'):
    for fname in files:
        path = os.path.join(root, fname)
        try:
            with open(path, errors='ignore') as f:
                content = f.read()
            if 'settings-general-days_to_upgrade_subs' not in content:
                continue
            new = re.sub(
                r'(settings-general-days_to_upgrade_subs.{0,200}?)max:30',
                lambda m: m.group(1) + 'max:300',
                content, flags=re.DOTALL
            )
            if new != content:
                with open(path, 'w') as f:
                    f.write(new)
                print('Patched:', path)
            else:
                print('No match found in:', path)
        except Exception as e:
            print('Error:', path, e)
