import ui, constInfo, event, net

class WarpDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.qid = 0
		self.objY = 40
		self.obj = {}
		self.categoryCount = 0
		self.page = 0
		self.pages = 1
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/warpwindow.py")

		except:
			import exception
			exception.Abort("WarpDialog.__LoadScript.LoadObject")

		try:
			self.board = self.GetChild("Board")
			self.prevButton = self.GetChild("PrevButton")
			self.nextButton = self.GetChild("NextButton")
		except:
			import exception
			exception.Abort("WarpDialog.__LoadScript.BindObject")

		ui.ScriptWindow.SetCenterPosition(self)
		self.board.SetCloseEvent(self.Hide)
		self.prevButton.SetEvent(ui.__mem_func__(self.SetPage), -1)
		self.nextButton.SetEvent(ui.__mem_func__(self.SetPage), 1)

	def AppendCategory(self, name, maps):

		if self.categoryCount > 0 and self.categoryCount % 3 == 0:
			self.objY = 40
			self.pages += 1

		self.obj[self.categoryCount] = {}

		self.obj[self.categoryCount]["bar"] = ui.HorizontalBar()
		self.obj[self.categoryCount]["bar"].SetParent(self)
		self.obj[self.categoryCount]["bar"].Create(420)
		self.obj[self.categoryCount]["bar"].Show()
		self.obj[self.categoryCount]["bar"].SetPosition(40, self.objY)

		self.obj[self.categoryCount]["text"] = ui.TextLine()
		self.obj[self.categoryCount]["text"].Show()
		self.obj[self.categoryCount]["text"].SetHorizontalAlignCenter()
		self.obj[self.categoryCount]["text"].SetVerticalAlignCenter()
		self.obj[self.categoryCount]["text"].SetParent(self.obj[self.categoryCount]["bar"])
		self.obj[self.categoryCount]["text"].SetText(name.replace("_", " "))
		self.obj[self.categoryCount]["text"].SetPosition(210, 7)
		self.objY += -10


		for i in xrange(len(maps.split("#"))):
			if i % 2 == 0:
				self.objY += 30
				x = 52
			else:
				x = 270
			self.obj[self.categoryCount]["button%d" % i] = ui.Button()
			self.obj[self.categoryCount]["button%d" % i].SetParent(self)
			self.obj[self.categoryCount]["button%d" % i].SetBasicVisualPath("d:/ymir work/ui/public/xlarge_Button_0%d.sub")
			self.obj[self.categoryCount]["button%d" % i].Show()
			self.obj[self.categoryCount]["button%d" % i].SetPosition(x, self.objY)
			self.obj[self.categoryCount]["button%d" % i].SetText(maps.split("#")[i].replace("_", " "))
			self.obj[self.categoryCount]["button%d" % i].SetEvent(ui.__mem_func__(self.Warp), self.categoryCount, i)

		if i % 2 == 0:
			self.obj[self.categoryCount]["button%d" % i].SetPosition(161, self.objY)

		self.objY += 30

		if self.pages == 1:
			self.prevButton.SetPosition(-30, self.objY)
			self.prevButton.SetWindowHorizontalAlignCenter()
			self.nextButton.SetPosition(30, self.objY)
			self.nextButton.SetWindowHorizontalAlignCenter()
			self.objY += 20
			self.board.SetSize(500, self.objY + 5)
			self.SetSize(500, self.objY + 5)
			self.SetCenterPosition()

		self.categoryCount += 1

		self.ShowPage(0)

	def SetPage(self, index):
		if index == 1:
			if self.page <= self.pages:
				self.page += 1
		else:
			if self.page > 0:
				self.page -= 1
		self.ShowPage(self.page)

	def ShowPage(self, index):
		for i in range(self.categoryCount):
			self.obj[i]["bar"].Hide()
			self.obj[i]["text"].Hide()
			button = 0
			while (self.obj[i].has_key("button%d" % button)):
				self.obj[i]["button%d" % button].Hide()
				button += 1

		for i in range(index*3, min((index*3)+3, self.categoryCount)):
			self.obj[i]["bar"].Show()
			self.obj[i]["text"].Show()
			button = 0
			while (self.obj[i].has_key("button%d"%button)):
				self.obj[i]["button%d"%button].Show()
				button += 1

	def Warp(self, category, index):
		self.Hide()
		constInfo.INPUT_DATA = "warp|%d|%d" % (category, index)
		self.QuestCmd()

	def QuestCmd(self):
		event.QuestButtonClick(self.qid)
		net.SendQuestInputStringPacket(constInfo.INPUT_DATA)

	def SetQid(self, qid):
		self.qid = int(qid)

	def Destroy(self):
		self.ClearDictionary()

	def OpenWindow(self):
		if self.IsShow():
			self.Hide()
		else:
			self.Show()

	def OnPressEscapeKey(self):
		self.Hide()
		return True
