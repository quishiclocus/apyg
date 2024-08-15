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
        packages.shaka-packager =
          let
            version = "0.9.1";
            inherit (pkgs) stdenv lib;
          in
          stdenv.mkDerivation
            {
              name = "shaka-packager-${version}";

              # https://nixos.wiki/wiki/Packaging/Binaries
              src = pkgs.fetchurl {
                url =
                  "https://github.com/shaka-project/shaka-packager/releases/download/v${version}/packager-linux-x64";
                sha256 = "sha256-MoMX6PEtvPmloXJwRpnC2lHlT+tozsV4dmbCqweyyI0=";
              };

              dontUnpack = true;
              sourceRoot = ".";

              installPhase = ''
                install -m755 -D $src $out/bin/shaka-packager
              '';

              meta = with nixpkgs.lib; {
                homepage = "https://shaka-project.github.io/shaka-packager/html/";
                description =
                  "Media packaging framework for VOD and Live DASH and HLS applications";
                platforms = platforms.linux;
              };
            };
      }
    );
}
