Name:      rasa-power-client
Version:   2.2.0
Release:   0
Url:       https://github.com/warwick-one-metre/powerd
Summary:   Power system client for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-observatory-power

%description
Part of the observatory software for the RASA prototype telescope.

power is a commandline utility that interfaces with the power system daemon.
light is a commandline utility to swith the dome light on and off.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/power %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/light %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/rasa_power %{buildroot}/etc/bash_completion.d/power
%{__install} %{_sourcedir}/completion/light %{buildroot}/etc/bash_completion.d/light

%files
%defattr(0755,root,root,-)
%{_bindir}/power
%{_bindir}/light
/etc/bash_completion.d/power
/etc/bash_completion.d/light

%changelog