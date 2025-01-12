%global debug_package %{nil}
%undefine __brp_add_determinism

%define name jetbrains-intellij-idea-ultimate
%define exclusivearch x86_64
%define rel 2024.2.3
%define srcfilename ideaIU-%{rel}.tar.gz

%define _ideadir %{_libdir}/%{name}

Name:          %{name}
Version:       %{rel}
Release:       1%{?dist}
Summary:       JetBrains Java IDE

License:       Commercial
URL:           https://www.jetbrains.com/idea
Source0:       https://download.jetbrains.com/idea/%{srcfilename}#/%{name}-%{version}.tar.gz
Source10:      jetbrains.desktop

ExclusiveArch: %{exclusivearch}
Requires:      java
BuildRequires: desktop-file-utils
Conflicts:     %{name}
Provides:      %{name} = %{version}

%description
JetBrains Java IDE

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{_ideadir}
cp -r idea-IU-*/* %{buildroot}%{_ideadir}/
install -d %{buildroot}%{_bindir}
ln -s "$(realpath -m --relative-to %{_bindir}/%{name} %{_ideadir}/idea)" %{buildroot}%{_bindir}/%{name}

install -Dm644 %{SOURCE10} %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-edit \
  --set-name="IntelliJ IDEA Ultimate" \
  --set-comment="JetBrains Java IDE" \
  --set-icon=%{name} \
  --set-key=Exec \
  --set-value=%{name} \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm644 idea-IU-*/bin/idea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%{_ideadir}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

%changelog
* Sun Jan 12 2025 dusansimic <dusan.simic1810@gmail.com> - 2024.2.3
- Release 2024.2.3
