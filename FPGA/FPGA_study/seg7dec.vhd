library IEEE;
use IEEE.std_logic_1164.all;

entity dec_7seg is
	port(
		SW		:	in std_logic_vector(3 downto 0);
		HEX0	:	out std_logic_vector(6 downto 0)
	);
end dec_7seg;

architecture RTL of dec_7seg is

begin
	process(SW)
	begin
		case SW is
			when "0000"	=>	HEX0	<=	"1000000";
			when "0001"	=>	HEX0	<=	"1111001";
			when "0010"	=>	HEX0	<=	"0100100";
			when "0011"	=>	HEX0	<=	"0110000";
			when "0100"	=>	HEX0	<=	"0011001";
			when "0101"	=>	HEX0	<=	"0010010";
			when "0110"	=>	HEX0	<=	"0000010";
			when "0111"	=>	HEX0	<=	"1111000";
			when "1000"	=>	HEX0	<=	"0000000";
            when "1001"	=>	HEX0	<=	"0010000";
            when "1010" =>  HEX0    <=  "0001000";
            when "1011" =>  HEX0    <=  "0000011";
            when "1100" =>  HEX0    <=  "1000110";
            when "1101" =>  HEX0    <=  "0100001";
            when "1110" =>  HEX0    <=  "0000110";
            when "1111" =>  HEX0    <=  "0001110";
			when others	=>	HEX0	<=	"1111111";
		end case;
	end process;
end RTL;