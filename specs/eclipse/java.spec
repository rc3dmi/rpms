%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

%define name eclipse-java
%define exclusivearch x86_64
%define rel 2024-09/R
%define reldash 2024-09-R
%define srcfilename %{name}-%{reldash}-linux-gtk-%{exclusivearch}.tar.gz

%define _eclipsedir %{_libdir}/%{name}

Name:           %{name}
Version:        4.33
Release:        1%{?dist}
Summary:        Highly extensible IDE (Java version)

License:        EPL
URL:            https://www.eclipse.org
Source0:        %{url}/downloads/download.php?file=/technology/epp/downloads/release/%{rel}/%{srcfilename}&r=1#/%{name}-%{version}.tar.gz
Source10:       eclipse.desktop

ExclusiveArch:  %{exclusivearch}
Requires:       java
BuildRequires:  desktop-file-utils
Conflicts:      %{name}
Provides:       %{name} = %{version}

%description
The essential tools for any Java developer, including a Java IDE, a CVS client, Git client, XML Editor, Mylyn, Maven integration and WindowBuilder

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{_libdir}
cp -r eclipse %{buildroot}%{_eclipsedir}
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/%{name} %{_libdir}/%{name}/eclipse)" %{buildroot}%{_bindir}/%{name}

install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-edit \
  --set-name="Eclipse (Java)" \
  --set-comment="Java development environment" \
  --set-icon=%{name} \
  --set-key=Exec \
  --set-value=%{name} \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

for i in 16 22 24 32 48 64 128 256 512 1024 ; do
  install -Dm644 eclipse/plugins/org.eclipse.platform_%{version}*/"eclipse$i.png" "%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png"
done

find %{buildroot}%{_eclipsedir}/plugins/com.sun.jna_5.13.0.v20230812-1000/com/sun/jna -type d ! -iname '*linux-x86-64' ! -iname '*jna' | xargs rm -rf

%files
%{_eclipsedir}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Mon Oct 14 2024 dusansimic <dusan.simic@dmi.uns.ac.rs> - 4.33-1
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