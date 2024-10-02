using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PharmacyManagementSystem
{
    public partial class StartingPage : Form
    {

        public StartingPage()
        {
            InitializeComponent();
            circlepbar2.Value = 0;
        }
        private void StartingPage_Load(object sender, EventArgs e)
        {

        }
       

        private void timer2_Tick_1(object sender, EventArgs e)
        {
            circlepbar2.Value += 1;
            
            if (circlepbar2.Value == 100)
            {
                circlepbar2.Value = 0;
                timer22.Stop();
                this.Hide();
                Login login = new Login();
                login.Show();
                this.Hide();
            }
        }
    }
}
