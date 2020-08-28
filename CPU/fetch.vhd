library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity fetch is
    port
    (
        CLK_FT      :   in std_logic;
        P_COUNT     :   in std_logic_vector(7 downto 0);
        PROM_OUT    :   out std_logic_vector(14 downto 0)
    );
end fetch;

architecture RTL of fetch is

subtype WORD is std_logic_vector(14 downto 0);

type MEMORY is array (0 to 15) of WORD;

constant MEM    :   MEMORY   :=
    (
        "100100000000000",
    )