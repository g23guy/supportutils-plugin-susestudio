#
# spec file for package supportutils-plugin-susestudio (Version 0.0-0)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-susestudio
URL:          https://code.google.com/p/supportutils-plugin-susestudio/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      0
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for SUSE Studio
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource-0.0.1
Requires:     susestudio

%description
Extends supportconfig functionality to include system information about 
SUSE Studio. The supportconfig saves the plugin output to plugin-susestudio.txt.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-susestudio/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f susestudio-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0500 susestudio $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 susestudio-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/susestudio-plugin.8.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/*
/usr/share/man/man8/susestudio-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-susestudio

