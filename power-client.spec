Name:      onemetre-power-client
Version:   1.0
Release:   1
Url:       https://github.com/warwick-one-metre/powerd
Summary:   Power system client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3

%description
Part of the observatory software for the Warwick one-meter telescope.

power is a commandline utility that interfaces with the power system daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/power %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/power %{buildroot}/etc/bash_completion.d/power

# Install python dependencies
# This is horrible, but it seems to be the only way that actually works!
pip3 install Pyro4

%files
%defattr(0755,root,root,-)
%{_bindir}/power
/etc/bash_completion.d/power

%changelog
