Name:      observatory-power-client
Version:   20210608
Release:   0
Url:       https://github.com/warwick-one-metre/powerd
Summary:   Power system client.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-power

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/power %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/light %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/power %{buildroot}/etc/bash_completion.d/power
%{__install} %{_sourcedir}/completion/light %{buildroot}/etc/bash_completion.d/light

%files
%defattr(0755,root,root,-)
%{_bindir}/power
%{_bindir}/light
/etc/bash_completion.d/power
/etc/bash_completion.d/light

%changelog
