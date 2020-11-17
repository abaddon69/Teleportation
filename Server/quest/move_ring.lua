quest warp begin
	state start begin
		function info()
			local tab = {
				[1] = {
					["name"] = "Pierwsze wioski",
					["maps"] = {
						{"Shinsoo", 474300, 954800, 1},
						{"Chunjo", 63800, 166400, 1},
						{"Jinno", 959900, 269200, 1},
						{"Shinsoo M2", 353100, 882900, 1},
						{"Chunjo M2", 145500, 240000, 1},
						{"Jinno M2", 863900, 246000, 1},
					},
				},
				[2] = {
					["name"] = "Krainy",
					["maps"] = {
						{"Dolina Orków", 332600, 746800, 1},
						{"Pustynia Yongbi", 295600, 548100, 1},
						{"Œwi¹tynia Hwang", 553600, 143600, 1},
						{"Góra Sohan", 434700, 214200, 1},
						{"Ognista Ziemia", 604600, 692600, 1}, 
					},
				},
				[3] = {
					["name"] = "Dzikie Krainy",
					["maps"] = {
						{"Loch paj¹ków v1", 60000, 496000, 15},
						{"Loch paj¹ków v2", 665600, 435200, 15},
						{"Czerwony las", 1119900, 70800, 15},
						{"Trolle", 221900, 9300, 60},
						{"Zombie", 135600, 4300, 80},
						{"Dzikia Ziemia", 1189600, 11646100, 145},
						{"Burzowe Góry", 1253200, 1253300, 180},
						{"Lodowa Pieœñ", 512000, 153600, 210},
						{"Diabelskie Katakumby", 8007600, 6600, 230},
					},
				},
				[4] = {
					["name"] = "Grota wygnañców",
					["maps"] = {
						{"V1", 9800, 1215100, 55},
						{"V2", 153600, 1203200, 70},
						{"V3", 0, 1356800, 75},
						{"V4", 153600, 1356800, 85},
						{"V5", 0, 1510400, 100},
						{"V6", 153600, 1510400, 110},
						{"V7", 0, 1664000, 120},
						{"V8", 153600, 1664000, 130},
						{"V9", 0, 2203200, 140},
						{"V10", 99800, 941200, 200},
						{"V11", 5994500, 9548900, 220},
					},
				},
				[5] = {
					["name"] = "Inne",
					["maps"] = {
						{"Wie¿a Demonów", 590500, 110500, 40},
						{"Ziemia Olbrzymów", 845100, 745900, 75},
					},
				},
			}
			return tab
		end
		function send_maps()
			local tab = warp.info()
			for i=1, table.getn(tab) do
				local maps = ""
				for j=1, table.getn(tab[i]["maps"]) do
					local add = "#"
					if j == table.getn(tab[i]["maps"]) then
						add = ""
					end
					map_name = tab[i]["maps"][j][1]
					if tab[i]["maps"][j][4] > 1 then
						map_name = map_name.."_|cfffff400"..tab[i]["maps"][j][4].." +|h|r"
					end
					maps = maps..string.gsub(map_name, " ", "_")..add
				end
				build_cmd("WarpAppendCategory", string.gsub(tab[i]["name"], " ", "_"), maps)
			end
		end
		when login begin
			build_cmd("WarpSetQid", q.getcurrentquestindex())
			warp.send_maps()
		end
		when button or info begin
			local cmd = string.split(get_input("GetInput"), "|")
			if cmd[1] == "warp" then
				tab = warp.info()
				map = tab[tonumber(cmd[2])+1]["maps"][tonumber(cmd[3])+1]
				if map == nil then return end
				if pc.get_level() >= map[4] then
					pc.warp(map[2], map[3])
				end
			end
		end
	end
end