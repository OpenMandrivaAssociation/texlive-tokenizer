# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tokenizer
# catalog-date 2006-12-23 09:07:09 +0100
# catalog-license lppl
# catalog-version 1.1.0
Name:		texlive-tokenizer
Version:	1.1.0
Release:	1
Summary:	A tokenizer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tokenizer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tokenizer.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A tokenizer for LaTeX. \GetTokens{Target1}{Target2}{Source}
Splits Source into two tokens at the first encounter of a
comma. The first token is saved in a newly created command with
the name passed as Target1 and the second token likewise. A
package option 'trim' causes leading and trailing space to be
removed from each token; with this option, the \TrimSpaces
command is defined, which removes leading and trailing spaces
from its argument.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tokenizer/tokenizer.sty
%doc %{_texmfdistdir}/doc/latex/tokenizer/tokenizer.pdf
%doc %{_texmfdistdir}/doc/latex/tokenizer/tokenizer.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
