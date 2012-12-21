%define data_version 2012.12.21

Name:           command-not-found
Version:        1.0
Release:        1
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



%package -n     command-not-found-data
Version:        %{data_version}
Summary:        Data files for command-not-found
Group:          File tools

%description -n command-not-found-data
Contains data files for command-not-found tool.
This package will be rebuilt every week with new data.


%prep
%setup -q -n %{name}

%install
mkdir -p %{buildroot}/usr/share/command-not-found
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/etc/profile.d
cp command-not-found.py  %{buildroot}/usr/lib/command-not-found
cp data.json %{buildroot}/usr/share/command-not-found/data.json
cp handler.sh %{buildroot}/etc/profile.d/91cnf.sh


%files
/usr/lib/command-not-found
/etc/profile.d/91cnf.sh

%files -n command-not-found-data
%dir /usr/share/command-not-found/
/usr/share/command-not-found/data.json
