library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity count10 is
    port(
        CLK :   in std_logic;
        RST :   in std_logic;
        COUNT   : out std_logic_vector(3 downto 0)
    );
end count10;

architecture RTL of count10 is

signal COUNT_TMP    :   std_logic_vector(3 downto 0);

begin
    process(CLK)
    begin
        if(CLK'event and CLK = '1') then
            if(RST = '1') then
                COUNT_TMP <= "0000";
            elsif(COUNT_TMP = "1001") then
                COUNT_TMP <= "0000";
            else
                COUNT_TMP <= COUNT_TMP + 1;
            end if;
        end if;
    end process;

    COUNT <= COUNT_TMP;

end RTL;
