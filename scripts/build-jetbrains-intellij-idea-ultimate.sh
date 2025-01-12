#!/bin/bash

set -eoux pipefail

rpmdev-setuptree

cp /ctx/specs/jetbrains/jetbrains.desktop ~/rpmbuild/SOURCES
cp /ctx/specs/jetbrains/*.spec ~/rpmbuild/SPECS

spectool -g -R ~/rpmbuild/SPECS/intellij-ultimate.spec
tree ~/rpmbuild/SOURCES

dnf --nodocs --assumeyes builddep ~/rpmbuild/SPECS/intellij-ultimate.spec

QA_RPATHS=$(( 0x0004|0x0008 )) rpmbuild -ba ~/rpmbuild/SPECS/intellij-ultimate.spec

tree ~/rpmbuild/RPMS
tree ~/rpmbuild/SRPMS
