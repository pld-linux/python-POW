%define		module	POW
#
Summary:	OpenSSL bindings for Python
Summary(pl.UTF-8):	Interfejs OpenSSL dla Pythona
Name:		python-%{module}
Version:	0.7
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pow/%{module}-%{version}.tar.gz
# Source0-md5:	e2d83a9f564cfd0ea1e1aa6488a05247
URL:		http://sourceforge.net/projects/pow/
BuildRequires:	openssl-devel >= 0.9.6
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to the OpenSSL library.

%description -l pl.UTF-8
Interfejs Pythona do biblioteki OpenSSL.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*.pdf
%dir %{py_sitedir}/POW
%{py_sitedir}/POW/*.py[co]
%attr(755,root,root) %{py_sitedir}/POW/*.so
