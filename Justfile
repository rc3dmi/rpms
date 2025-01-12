generate-tags fedora_release="":
  #!/bin/bash
  set -eoux pipefail

  BUILD_TAGS=()
  FEDORA_RELEASE_LATEST="$(jq -r '.["fedora_releases"].["latest"]' metainfo.json)"
  FEDORA_RELEASE_NEXT="$(jq -r '.["fedora_releases"].["next"]' metainfo.json)"

  if [ "{{ fedora_release }}" = "${FEDORA_RELEASE_LATEST}" ]
  then
    BUILD_TAGS+=("latest")
  elif [ "{{ fedora_release }}" = "${FEDORA_RELEASE_NEXT}" ]
  then
    BUILD_TAGS+=("next")
  fi

  BUILD_TAGS+=("{{ fedora_release }}")

  echo "${BUILD_TAGS[*]}"

generate-package-tags fedora_release="" package_name="":
  #!/bin/bash
  set -eoux pipefail

  BUILD_TAGS=()
  FEDORA_RELEASE_LATEST="$(jq -r '.["fedora_releases"].["latest"]' metainfo.json)"
  FEDORA_RELEASE_NEXT="$(jq -r '.["fedora_releases"].["next"]' metainfo.json)"
  PACKAGE_VERSION="$(jq -r '.["packages"].["{{ package_name }}"].["version"]' metainfo.json)"

  if [ "{{ fedora_release }}" = "${FEDORA_RELEASE_LATEST}" ]
  then
    BUILD_TAGS+=("latest" "${PACKAGE_VERSION}")
  elif [ "{{ fedora_release }}" = "${FEDORA_RELEASE_NEXT}" ]
  then
    BUILD_TAGS+=("next" "next-${PACKAGE_VERSION}")
  fi

  BUILD_TAGS+=("{{ fedora_release }} {{ fedora_release }}-${PACKAGE_VERSION}")

  echo "${BUILD_TAGS[*]}"
