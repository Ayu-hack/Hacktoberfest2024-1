using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PharmacyManagementSystem
{
    public partial class Login : Form
    {
        public Login()
        {
            InitializeComponent();
            PasswordTb.PasswordChar = '\u25CF';
        }
        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");

        public static string User;
        private void label2_Click(object sender, EventArgs e)
        {
            AdminLogin adminLoginobj = new AdminLogin();
            adminLoginobj.Show();
            this.Hide();
        }

        private void LoginBtn_Click(object sender, EventArgs e)
        {
            if(UnameTb.Text== "" || PasswordTb.Text == "")
            {
                MessageBox.Show("Enter Both Username & Passkey");
            }
            else
            {
                conn.Open();
                SqlDataAdapter sda = new SqlDataAdapter("Select Count(*) from SellerTbl where SellerName='"+UnameTb.Text+"' and SellerPassword='"+PasswordTb.Text+"'",conn);
                DataTable dt = new DataTable();
                sda.Fill(dt);
                if (dt.Rows[0][0].ToString() == "1")
                {
                    User = UnameTb.Text;
                    Sellings sellingsobj = new Sellings();
                    sellingsobj.Show();
                    this.Hide();
                    conn.Close();
                }
                else
                {
                    MessageBox.Show("Wrong UserName OR Password");

                }

                conn.Close();
            }
        }

        private void Login_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
