window = {
	"name" : "WarpDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 500,
	"height" : 300,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"title" : "Teleportacja",

			"width" : 500,
			"height" : 300,

			"children" : (
				{
					"name": "PrevButton",
					"type": "button",

					"x": 0,
					"y": 0,

					"default_image": "d:/ymir work/ui/privatesearch/private_prev_btn_01.sub",
					"over_image": "d:/ymir work/ui/privatesearch/private_prev_btn_02.sub",
					"down_image": "d:/ymir work/ui/privatesearch/private_prev_btn_01.sub",
				},
				{
					"name": "NextButton",
					"type": "button",

					"x": 0,
					"y": 0,

					"default_image": "d:/ymir work/ui/privatesearch/private_next_btn_01.sub",
					"over_image": "d:/ymir work/ui/privatesearch/private_next_btn_02.sub",
					"down_image": "d:/ymir work/ui/privatesearch/private_next_btn_01.sub",
				},
			),
		},
	),
}