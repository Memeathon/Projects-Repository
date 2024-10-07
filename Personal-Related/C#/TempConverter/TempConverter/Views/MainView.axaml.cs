using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.Metadata;
using System;
using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;

namespace HermesHub.Views;

public partial class MainView : UserControl
{
    string LastInput = "";
    public MainView()
    {
        InitializeComponent();
    }

    public void ButtonClicked(object source, RoutedEventArgs args)
    {
        if ( LastInput != "fahrenheit" && Double.TryParse(celsius.Text, out double C))
        {
            var F = C * (9 / 5) + 32;
            fahrenheit.Text = F.ToString("0.0");
        }
        else if ( LastInput == "fahrenheit" && Double.TryParse(fahrenheit.Text, out double F))
        {
            C = F * (9 / 5) - 32;
            celsius.Text = C.ToString("0.0");
        }
    }
    public void TextBox_KeyUp(object? sender, Avalonia.Input.KeyEventArgs e)
    {
        if (celsius.Text != null && !celsius.Text.Contains('.'))
        {
            celsius.Text += ".0";
        }
        if (fahrenheit.Text != null && !fahrenheit.Text.Contains('.'))
        {
            fahrenheit.Text += ".0";
        }
    }
    private void Fahrenheit_TextChanged(object? sender, Avalonia.Controls.TextChangedEventArgs e)
    {
        LastInput = "fahrenheit";
    }
    private void Celsius_TextChanged(object? sender, Avalonia.Controls.TextChangedEventArgs e)
    {
        LastInput = "celsius";
    }
}
