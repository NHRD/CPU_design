library IEEE;
use IEEE.std_logic_1164.all

entity dec_7seg is
	port(
		DIN		:	in std_logic_vector(3 downto 0);
		SEG7	:	out std_logic_vector(6 downto 0)
	);
end dec_7seg;

architecture RTL of dec_7seg is
	begin
		process(DIN)
		begin
			case DIN is
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
				when "0000"	=>	SEG7	<=	"100000";
