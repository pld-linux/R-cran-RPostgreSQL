%define		fversion	%(echo %{version} | tr r -)
%define		modulename	RPostgreSQL
%define		_noautoreq	/usr/bin/r
Summary:	R PostgreSQL Database Interface
Name:		R-cran-%{modulename}
Version:	0.4
Release:	2
License:	GPL
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	6f9e63f9f5818645171212a40324fccc
BuildRequires:	R >= 2.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Database interface and PostgreSQL driver for R This version complies with
the database interface definition as implemented in the package DBI.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
