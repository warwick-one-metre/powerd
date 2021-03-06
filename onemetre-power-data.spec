Name:      onemetre-power-data
Version:   20210608
Release:   0
Url:       https://github.com/warwick-one-metre/powerd
Summary:   Power system configuration files.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/powerd/

%{__install} %{_sourcedir}/10-onemetre-power.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/powerd/

%files
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-onemetre-power.rules
%{_sysconfdir}/powerd/onemetre.json

%changelog
