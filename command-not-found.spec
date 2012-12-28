Name:           command-not-found
Version:        1.0
Release:        2
Summary:        Command-not-found tool for ROSA
Group:          File tools
License:        GPLv2
URL:            N/A
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       command-not-found-data
Requires:       python-json

%description
When you call non-existent command in bash, you will get a 
list of packages (with repositories) where you can find this command
or similar ones.

%prep
%setup -q -n %{name}


%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/profile.d
cp command-not-found.py  %{buildroot}/usr/bin/cnf
cp handler.sh %{buildroot}/etc/profile.d/91cnf.sh
%find_lang %{name}

%files -f %{name}.lang
/usr/bin/cnf
/etc/profile.d/91cnf.sh
