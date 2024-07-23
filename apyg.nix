let
  pkgs = import <nixpkgs> { };
  mkDerivation = import ./autotools.nix pkgs;
in
mkDerivation {
  name = "apyg";
  src = builtins.fetchGit {
    url = "git@github.com:quishiclocus/apyg.git";
    ref = "master";
  };
}
