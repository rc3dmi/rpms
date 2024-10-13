%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

%define eclusivearch x86_64
%define rel 2024-09/R
%define reldash 2024-09-R

Name:           eclipse
Version:        4.33
Release:        1%{?dist}

License:        EPL
URL:            https://www.eclipse.org

Source1:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/eclipse-java-%{reldash}-linux-gtk-%{eclusivearch}.tar.gz&r=1#/eclipse-java-%{version}.tar.gz
Source2:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/eclipse-jee-%{reldash}-linux-gtk-%{eclusivearch}.tar.gz&r=1#/eclipse-jee-%{version}.tar.gz
Source3:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/eclipse-cpp-%{reldash}-linux-gtk-%{eclusivearch}.tar.gz&r=1#/eclipse-cpp-%{version}.tar.gz

Source10:       eclipse.desktop

ExclusiveArch:  %{exclusivearch}
Requires:       java
BuildRequires:  desktop-file-utils

%description
The essential tools for any Java developer, including a Java IDE, a CVS client, Git client, XML Editor, Mylyn, Maven integration and WindowBuilder

%package java
Summary:        Highly extensible IDE (Java version)

%package jee
Summary:        Highly extensible IDE (JEE version)

%package cpp
Summary:        Highly extensible IDE (C++ version)

%prep
%setup -c -T
mkdir eclipse-java
tar -xzf %{SOURCE1} -C eclipse-java
mkdir eclipse-jee
tar -xzf %{SOURCE2} -C eclipse-jee
mkdir eclipse-cpp
tar -xzf %{SOURCE3} -C eclpise-cpp

%build

%install
# eclipse-java
## install files
install -d %{buildroot}%{_libdir}
cp -r eclipse-java/eclipse %{buildroot}%{_libdir}/eclipse-java
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/eclipse-java %{_libdir}/eclipse-java/eclipse)" %{buildroot}%{_bindir}/eclipse-java

## install desktop file
install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/applications/eclipse-java.desktop
desktop-file-edit \
  --set-name="Eclipse (Java)" \
  --set-comment="Java development environment" \
  --set-icon=eclipse-java \
  --set-key=Exec \
  --set-value=eclipse-java \
  %{buildroot}%{_datadir}/applications/eclipse-java.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/eclipse-java.desktop

## install icons
for i in 16 22 24 32 48 64 128 256 512 1024 ; do
  install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/eclipse-java.png"
done

## cleanup
find %{buildroot}%{_libdir}/eclipse-java/plugins/com.sun.jna_5.13.0.v20230812-1000/com/sun/jna -type d ! -iname '*linux-x86-64' ! -iname '*jna' | xargs rm -rf



# eclipse-jee
## install files
install -d %{buildroot}%{_libdir}
cp -r eclipse-jee/eclipse %{buildroot}%{_libdir}/eclipse-jee
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/eclipse-jee %{_libdir}/eclipse-jee/eclipse)" %{buildroot}%{_bindir}/eclipse-jee

## install desktop file
install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/applications/eclipse-jee.desktop
desktop-file-edit \
  --set-name="Eclipse (JEE)" \
  --set-comment="JEE development environment" \
  --set-icon=eclipse-jee \
  --set-key=Exec \
  --set-value=eclipse-jee \
  %{buildroot}%{_datadir}/applications/eclipse-jee.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/eclipse-jee.desktop

## install icons
for i in 16 22 24 32 48 64 128 256 512 1024 ; do
  install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/eclipse-jee.png"
done

## cleanup
find %{buildroot}%{_libdir}/eclipse-jee/plugins/com.sun.jna_5.13.0.v20230812-1000/com/sun/jna -type d ! -iname '*linux-x86-64' ! -iname '*jna' | xargs rm -rf



# eclipse-cpp
## install files
install -d %{buildroot}%{_libdir}
cp -r eclipse-cpp/eclipse %{buildroot}%{_libdir}/eclipse-cpp
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/eclipse-cpp %{_libdir}/eclipse-cpp/eclipse)" %{buildroot}%{_bindir}/eclipse-cpp

## install desktop file
install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/applications/eclipse-cpp.desktop
desktop-file-edit \
  --set-name="Eclipse (Java)" \
  --set-comment="Java development environment" \
  --set-icon=eclipse-cpp \
  --set-key=Exec \
  --set-value=eclipse-cpp \
  %{buildroot}%{_datadir}/applications/eclipse-cpp.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/eclipse-cpp.desktop

## install icons
for i in 16 22 24 32 48 64 128 256 512 1024 ; do
  install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/eclipse-cpp.png"
done

## cleanup
find %{buildroot}%{_libdir}/eclipse-cpp/plugins/com.sun.jna_5.13.0.v20230812-1000/com/sun/jna -type d ! -iname '*linux-x86-64' ! -iname '*jna' | xargs rm -rf




%files java
%{libdir}/eclipse-java
%{_bindir}/eclipse-java
%{_datadir}/applications/eclipse-java.desktop
%{_datadir}/icons/hicolor/*/apps/eclipse-java.png

%files jee
%{libdir}/eclipse-jee
%{_bindir}/eclipse-jee
%{_datadir}/applications/eclipse-jee.desktop
%{_datadir}/icons/hicolor/*/apps/eclipse-jee.png

%files cpp
%{libdir}/eclipse-cpp
%{_bindir}/eclipse-cpp
%{_datadir}/applications/eclipse-cpp.desktop
%{_datadir}/icons/hicolor/*/apps/eclipse-cpp.png

%changelog
* Sun Oct 13 2024 dusansimic <dusan.simic@dmi.uns.ac.rs> - 4.33-1
- Release 4.33
- Modify for use in computer lab
* Sat Oct 14 2023 manojbaishya <28330014+manojbaishya@users.noreply.github.com> - 4.30-1
- Release 4.30
* Sat Oct 14 2023 manojbaishya <28330014+manojbaishya@users.noreply.github.com> - 4.29-1
- Release 4.29
- Add cleanup command for removing directories for different platforms
* Wed Mar 22 2023 dusansimic <dusan.simic1810@gmail.com> - 4.27-1
- Release 4.27
* Mon Dec 26 2022 dusansimic <dusan.simic1810@gmail.com> - 4.26-1
- Release 4.26
* Mon Oct 10 2022 dusansimic <dusan.simic1810@gmail.com> - 4.25-1
- Release 4.25
* Mon Aug 15 2022 dusansimic <dusan.simic1810@gmail.com> - 4.24-1
- Release 4.24
* Fri Dec 10 2021 dusansimic <dusan.simic1810@gmail.com> - 4.22-1
- Release 4.22
* Thu Nov  4 2021 dusansimic <dusan.simic1810@gmail.com> - 4.21-1
- Release 4.21
