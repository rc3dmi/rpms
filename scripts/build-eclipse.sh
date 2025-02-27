#!/bin/bash

set -eoux pipefail

rpmdev-setuptree

cp /ctx/specs/eclipse/eclipse.desktop ~/rpmbuild/SOURCES
cp /ctx/specs/eclipse/*.spec ~/rpmbuild/SPECS

spectool -g -R ~/rpmbuild/SPECS/java.spec
spectool -g -R ~/rpmbuild/SPECS/jee.spec
tree ~/rpmbuild/SOURCES

dnf --nodocs --assumeyes builddep ~/rpmbuild/SPECS/java.spec
dnf --nodocs --assumeyes builddep ~/rpmbuild/SPECS/jee.spec

rpmbuild -ba ~/rpmbuild/SPECS/java.spec
rpmbuild -ba ~/rpmbuild/SPECS/jee.spec

tree ~/rpmbuild/RPMS
tree ~/rpmbuild/SRPMS
