provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "webapp-rg"
  location = "East US"
}

resource "azurerm_app_service_plan" "app_service_plan" {
  name                = "webapp-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "app_service" {
  name                = "webapp-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.app_service_plan.id
}