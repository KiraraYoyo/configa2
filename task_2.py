import yaml
import urllib.request
import json

def get_dependencies(package_name, version, url):
    url = f"{url}/{package_name}/{version}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            package_info = json.loads(data)
            dependencies = package_info.get('dependencies', {})
            
            print(f"Прямые зависимости для {package_name}@{version}:")
            for dep, version_range in dependencies.items():
                print(f"- {dep}: {version_range}")
                
            return dependencies
            
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        return {}
    
with open('config.yaml') as f:
    config = yaml.safe_load(f)
    

if not isinstance(config["maxDepth"], int):
    print("ERROR: maxDepth needs to be integer")
elif config["maxDepth"] < 1:
    print("ERROR: maxDepth needs to be positive")
for x in config:
    if config[x] is None:
        print("ERROR:", x, "is empty")

get_dependencies(config["name"], config["version"], config["repoURL"])

