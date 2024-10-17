%define		_class		PHP
%define		_subclass	Parser
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.2.2
Release:	2
Summary:	A PHP grammar parser
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/PHP_Parser/
Source0:	http://download.pear.php.net/package/PHP_Parser-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
PHP_Parser is a source code analysis tool based around a real Parser
generated by phpJay. The parser uses the same EBNF source that PHP
uses to parse itself, and it therefore as robust as PHP itself.
This version has full support for parsing out every re-usable element
in PHP 5 as of beta 1:
- classes
- abstract classes
- inheritance, implements
- interfaces
- methods
- exception parsing directly from source
- static variables declared
- global and superglobal ($_GET) variables used
and declared
- variables
- constants
- functions (same information as methods)
- defines
- global variables (with help of the Tokenizer Lexer)
- superglobal variables used in global code
- include statements

The output can be customized to return an array, return
objects of user-specified classes, and can also be
customized to publish each element as it is parsed, allowing
hooks into parsing to catch information.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-6mdv2012.0
+ Revision: 742258
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-5
+ Revision: 679565
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-4mdv2011.0
+ Revision: 613757
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-3mdv2010.1
+ Revision: 467956
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.1-2mdv2010.0
+ Revision: 441560
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 368308
- Update php pear PHP_Parser to 0.2.1 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2009.1
+ Revision: 322653
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdv2009.0
+ Revision: 237052
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdv2008.0
+ Revision: 15963
- fix build
- 0.2.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2007.0
+ Revision: 82521
- Import php-pear-PHP_Parser

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdk
- initial Mandriva package (PLD import)


