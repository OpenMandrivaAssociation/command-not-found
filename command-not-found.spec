Name:           command-not-found
Version:        1.2
Release:        7
Summary:        Command-not-found tool for ROSA and OpenMandriva
Group:          File tools
License:        GPLv2
URL:            N/A
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       command-not-found-data
Requires:       python-json
Requires:       python-rpm
BuildRequires:  python(abi) = 2.7

%description
When you call non-existent command in bash, you will get a 
list of packages (with repositories) where you can find this command
or similar ones.

%prep
%setup -q -n %{name}
# Requires rpm bindings that haven't been ported yet
sed -i -e 's,/python,/python2,g' command-not-found.py
2to3 -w localizer.py

%install
for d in `python localizer.py --list`; do\
    mkdir -p %{buildroot}/usr/share/locale/$d/LC_MESSAGES;\
    install -m 644 locale/$d/LC_MESSAGES/%{name}.mo %{buildroot}/usr/share/locale/$d/LC_MESSAGES/%{name}.mo;\
done
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/profile.d
cp command-not-found.py  %{buildroot}/usr/bin/cnf
cp handler.sh %{buildroot}/etc/profile.d/91cnf.sh

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/cnf
/etc/profile.d/91cnf.sh
