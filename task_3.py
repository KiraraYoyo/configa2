import yaml
import urllib.request
import json
from collections import deque

def get_dependencies(package_name, vers, url, mode):
    if mode == "real":
        return get_real_dependencies(package_name, vers, url)
    elif mode == "test":
        return get_test_dependencies(package_name, vers, url)
    else:
        return {}

def get_real_dependencies(package_name, vers, url):
    if vers[0] == '~' or vers[0] == '^':
        version = vers[1:]
    else:
        version = vers
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

def get_test_dependencies(package_name, vers, url):
    if vers[0] == '~' or vers[0] == '^':
        version = vers[1:]
    else:
        version = vers
    url = f"{url}/{package_name}.{version}.npm"
    try:
        with open(url) as response:
            data = response.read()
            package_info = json.loads(data)
            dependencies = package_info.get('dependencies', {})
            
            print(f"Прямые зависимости для {package_name}@{version}:")
            for dep, version_range in dependencies.items():
                print(f"- {dep}: {version_range}")
                
            return dependencies
            
    except Exception as e:
        print(f"Ошибка при запросе: {e}")
        return {}

def dependency_graph(package, version, url, max_depth=None, mode="real"):
    visited = set()
    queue = deque([(package, version, 0)])
    dependency_graph = {}
    while queue:
        current_package, current_version, depth = queue.popleft()
        
        if depth >= max_depth:
            continue
            
        if current_package not in visited:
            visited.add(current_package)
            print(f"Анализируем: {current_package}@{current_version} (глубина: {depth})")
            
            dependencies = get_dependencies(current_package, current_version, url, mode)
            dependency_graph[current_package] = dependencies
            
            for dep_name, dep_version in dependencies.items():
                if dep_name not in visited:
                    queue.append((dep_name, dep_version, depth + 1))
    return dependency_graph

#///////////////////////////////////////////

with open('config.yaml') as f:
    config = yaml.safe_load(f)
config["version"] = str(config["version"])
if not isinstance(config["maxDepth"], int):
    print("ERROR: maxDepth needs to be integer")
elif config["maxDepth"] < 1:
    print("ERROR: maxDepth needs to be positive")
for x in config:
    if config[x] is None:
        print("ERROR:", x, "is empty")

dependency_graph(config["name"], config["version"], config["repoURL"], config["maxDepth"], config["mode"])

