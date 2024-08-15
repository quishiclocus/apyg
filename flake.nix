# in flake.nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        name = "simple";
        src = ./.;
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages.default = derivation {
          inherit system name src;
          builder = with pkgs; "${bash}/bin/bash";
          args = [ "-c" "echo foo > $out" ];
        };
        packages.apyg =
          let
            version = "0.9.1";
            inherit (pkgs) stdenv lib;
          in
          stdenv.mkDerivation
            {
              name = "apyg-${version}";

              # https://nixos.wiki/wiki/Packaging/Binaries
              src = pkgs.fetchurl {
                url =
                  "https://github.com/quishiclocus/apyg/releases/download/0.9.1-2/apyg-0.9.1.tar.gz";
                sha256 = "sha256-r4BuwWFbQU5q0HVg82vELe/UyX9A788IOZkGDYBZpDc=";
              };

              sourceRoot = ".";

              installPhase = ''
                python setup.py install
              '';

              buildPhase = ''
                python -m build
              '';

              sourcePhase = ''
                python -m build --sdist
              '';

              meta = with nixpkgs.lib; {
                homepage = "https://github.com/quishiclocus/apyg/";
                description =
                  "Generate random strings of varying length and complexity.";
              };
            };
      }
    );
}
