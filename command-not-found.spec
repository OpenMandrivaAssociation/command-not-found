Name:           command-not-found
Version:        1.3
Release:        8
Summary:        Command-not-found tool for ROSA and OpenMandriva
Group:          File tools
License:        GPLv2
URL:            https://abf.io/soft/command-not-found
Source0:        https://abf.io/soft/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:		cnf-1.3-dnf.patch
BuildArch:      noarch

Requires:       command-not-found-data
Requires:       python-json
Requires:       python-rpm
BuildRequires:  python(abi) >= 3.0

%description
When you call non-existent command in bash, you will get a 
list of packages (with repositories) where you can find this command
or similar ones.

%prep
%autosetup -p1
find . -name "*.py" |xargs 2to3 -w

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
