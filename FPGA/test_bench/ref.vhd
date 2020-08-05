library IEEE;
use IEEE.std_logic_1164.all;

entity and_or_sim is
end and_or_sim;

architecture SIM of and_or_sim is

component and_or
	port
	(
		A	: in std_logic;
		B	: in std_logic;
		Z_AND	: out std_logic;
		Z_OR	: out std_logic
	);
end component;

signal AT 	: std_logic;
signal BT 	: std_logic;
signal Z_ANDT	: std_logic;
signal Z_ORT 	: std_logic;

begin

	C1 : and_or
		port map(
			A => AT,
			B => BT,
			Z_AND => Z_ANDT,
			Z_OR => Z_ORT
		);	

    process begin
        
		AT <= '0';
		wait for 10 ns;
		AT <= '1';
        wait for 20 ns;
        
	end process;

    process begin
        
		BT <= '0';
		wait for 15 ns;
		BT <= '1';
        wait for 20 ns;
        
    end process;
    
end SIM;