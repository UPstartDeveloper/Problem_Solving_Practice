from collections import deque

dependencies = {
    "name": "my_cool_software",
    "version": "1.0.0",
    "dependencies": {
        "xmllib": {
            "version": "0.2.3",
            "name": "xmllib",
            "dependencies": {
                "parser": {"name": "parser", "version": "1.2.1"},
            },
        },
        "parser": {"name": "parser", "version": "1.4.6"},
    },
}


def flatten_dependencies(dependencies):
    # init a dict to map dependency names to their versions
    dependency_versions = dict()
    # init a stack
    next_dependencies = list()
    # place in the items of the dependencies dict from input
    for dependency in dependencies["dependencies"].values():
        next_dependencies.append(dependency)
    # begin DFS
    while next_dependencies:
        # pop the next software package from the stack
        next_dependency = next_dependencies.pop()
        # record its name and version number
        dependency_name, dependency_version = (
            next_dependency["name"],
            next_dependency["version"],
        )
        # put it in the dict - each dependency mapped to a set of versions needed
        if dependency_name in dependency_versions:
            dependency_versions[dependency_name].add(dependency_version)
        else:
            dependency_versions[dependency_name] = set([dependency_version])
        # push the items in its dependencies dict, if any
        if next_dependency.get("dependencies"):
            for dependency in next_dependency["dependencies"].values():
                next_dependencies.append(dependency)
    # return - expand into versions
    flattened_dependencies = dict()
    for dependency_name in dependency_versions:
        versions = dependency_versions[dependency_name]
        if len(versions) > 1:
            for version in versions:
                name_version = f"{dependency_name}@{version}"
                flattened_dependencies[name_version] = version
        else:
            flattened_dependencies[dependency_name] = versions.pop()
    return flattened_dependencies

    """
  dependencies = []
  """
