Name:           euca2ools
Version:        1.3.1
Release:        %mkrel 1
License:        BSD
Summary:        Elastic Utility Computing Architecture Command Line Tools
Url:            http://open.eucalyptus.com/downloads
Group:          Productivity/Networking/System
Source0:        %{name}-%{version}.tar.gz
Patch0:		euca2ools-1.3.1_Makefile.patch
BuildRequires:  make
BuildRequires:  python-boto   >= 1.9
BuildRequires:  python-devel
BuildRequires:  python-m2crypto
BuildRequires:  python-xmldiff
Requires:       python-base  >= 2.6
Requires:       python-boto  >= 1.9
Requires:       python-m2crypto
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Euca2ools are command-line tools for interacting with Web services that
export a REST/Query-based API compatible with Amazon EC2 and S3 services.
The tools can be used with both Amazon's services and with installations
of the Eucalyptus open-source cloud-computing infrastructure.

%prep
%setup -q
%patch0 -p0

%build
cd euca2ools
FLAGS="%{optflags}" python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a bin/* %{buildroot}%{_bindir}
cp -a man/* %{buildroot}%{_mandir}/man1
cd euca2ools
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc INSTALL COPYING README
%{_mandir}/man1/*
%{_bindir}/euca*
%{python_sitelib}/euca2ools*


