library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity count10_sim is
end count10_sim;

architecture SIM of count10_sim is

component count10
    port
    (
        CLK :   in std_logic;
        RST :   in std_logic;
        COUNT   :   out std_logic_vector(3 downto 0)
    );

end component;

signal CLK  :   std_logic;
signal RST  :   std_logic;
signal COUNT    :   std_logic_vector(3 downto 0);

begin

    C1 :   count10
        port map(
            CLK =>  CLK,
            RST =>  RST,
            COUNT => COUNT
        );

    process begin
        CLK <=  '0';
        wait for 10 ns;
        CLK <=  '1';
        wait for 10 ns;
    end process;

    process begin
        RST <= '1';
        wait for 15 ns;
        RST <= '0';
        wait;
    end process;
end SIM;
