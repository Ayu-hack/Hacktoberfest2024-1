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
    public partial class AdminLogin : Form
    {
        public AdminLogin()
        {
            InitializeComponent();
            AdminPassTb.PasswordChar = '*'; // Set PasswordChar property here

        }

        private void AdminLogin_Load(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void UnameTb_TextChanged(object sender, EventArgs e)
        {
           

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void PasswordTb_TextChanged(object sender, EventArgs e)
        {

        }

        private void bunifuThinButton21_Click(object sender, EventArgs e)
        {
            if (AdminPassTb.Text == "")
            {

            }
            else if (AdminPassTb.Text == "Admin")
            {

                Sellers sellerobj = new Sellers();
                sellerobj.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("Wrong Admin Password Credientials");
                AdminPassTb.Text = "";
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {
            
            Login login = new Login();
            login.Show();
            this.Hide();
        }
    }
}
