## search for:
import uiScriptLocale

## add under:
import uiwarp

## search for:
		self.wndGuildBuilding = None

## add under:
		self.wndWarp = None

## search for:
		self.dlgRefineNew = uiRefine.RefineDialogNew()
		self.dlgRefineNew.Hide()

## add under:
		self.wndWarp = uiwarp.WarpDialog()
		self.wndWarp.Hide()

## search for:
		self.wndChatLog.Destroy()

## add above:
		if self.wndWarp:
			self.wndWarp.Destroy()

## search for:
		del self.wndItemSelect

## add under:
		del self.wndWarp