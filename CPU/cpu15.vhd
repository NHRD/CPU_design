library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity cpu15 is
	port
	(
		CLK			:	in std_logic;
		RESET_N		:	in std_logic;
		IO65_IN		:	in std_logic_vector(15 downto 0);
		IO64_OUT	:	out std_logic_vector(15 downto 0)
	);
end cpu15;

architecture RTL of cpu15 is

--clock_gen
component clk_gen
	port
	(
		CLK			: 	in std_logic;
		CLE_FT		:	out std_logic;
		CLK_DC		:	out std_logic;
		CLK_EX		:	out std_logic;
		CLK_WB		:	out std_logic
	);
end component;

--fetch
component fetch
	port
	(
		CLK_FT		:	in std_logic;
		P_COUNT		:	in std_logic_vector(7 downto 0);
		PROM_OUT	:	out std_logic_vector(14 downto 0)
	);
end component;

--decode
component decode
	port
	(
		CLK_DC		:	in std_logic;
		PROM_OUT	:	in std_logic_vector(14 downto 0);
		OP_CODE		:	out std_logic_vector(3 downto 0);
		OP_DATA		:	out std_logic_vector(7 downto 0)
	);
end component;

--reg_dc
component reg_dc
	port
	(
		CLK_DC		:	in std_logic;
		N_REG_IN	:	in std_logic_vector(2 downto 0);
		REG_0		:	in std_logic_vector(15 downto 0);
		REG_1		:	in std_logic_vector(15 downto 0);
		REG_2		:	in std_logic_vector(15 downto 0);
		REG_3		:	in std_logic_vector(15 downto 0);
		REG_4		:	in std_logic_vector(15 downto 0);
		REG_5		:	in std_logic_vector(15 downto 0);
		REG_6		:	in std_logic_vector(15 downto 0);
		REG_7		:	in std_logic_vector(15 downto 0);
		N_REG_OUT	:	out std_logic_vector(2 downto 0);
		REG_OUT		:	out std_logic_vector(15 downto 0)
	);
end component;

--ram_dc
component ram_dc
	port
	(
		CLK_DC		:	in std_logic;
		RAM_AD_IN	:	in std_logic_vector(7 downto 0);
		RAM_0		:	in std_logic_vector(15 downto 0);
		RAM_1		:	in std_logic_vector(15 downto 0);
		RAM_2		:	in std_logic_vector(15 downto 0);
		RAM_3		:	in std_logic_vector(15 downto 0);
		RAM_4		:	in std_logic_vector(15 downto 0);
		RAM_5		:	in std_logic_vector(15 downto 0);
		RAM_6		:	in std_logic_vector(15 downto 0);
		RAM_7		:	in std_logic_vector(15 downto 0);
		IO65_IN		:	in std_logic_vector(15 downto 0);
		RAM_AD_OUT	:	out std_logic_vector(7 downto 0);
		RAM_OUT		:	out std_logic_vector(15 downto 0)
	);
end component;

--exec
component exec
	port
	(
		CLK_EX		:	in std_logic;
		RESET_N		:	in std_logic;
		OP_CODE		:	in std_logic_vector(3 downto 0);
		REG_A		:	in std_logic_vector(15 downto 0);
		REG_B		:	in std_logic_vector(15 downto 0);
		OP_DATA		:	in std_logic_vector(7 downto 0);
		RAM_OUT		:	in std_logic_vector(15 downto 0);
		P_COUNT		:	out std_logic_vector(7 downto 0);
		
	)
