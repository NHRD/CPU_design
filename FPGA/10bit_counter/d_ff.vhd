library IEEE;
use IEEE.std_logic_1164.all;

entity d_ff is
    port
    (
        CLK :   in std_logic;
        D   :   in std_logic;
        Q   :   out std_logic
    );
end d_ff;

architecture RTL of d_ff is

begin
    process(CLK)
    begin
        if(CLK'event and CLK = '1') then
            Q <= D;
        end if;
    end process;
end RTL;