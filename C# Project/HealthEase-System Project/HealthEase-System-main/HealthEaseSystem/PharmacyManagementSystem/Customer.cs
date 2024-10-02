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
    public partial class Customer : Form
    {
        public Customer()
        {
            InitializeComponent();
            ShowCust();
        }

        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");
        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void ShowCust()
        {
            conn.Open();
            string query = "Select * from CustomerTbl";
            SqlDataAdapter sda = new SqlDataAdapter(query, conn);
            SqlCommandBuilder Builder = new SqlCommandBuilder(sda);
            var ds = new DataSet();
            sda.Fill(ds);
            CustomerDGV.DataSource = ds.Tables[0];


            conn.Close();
        }
        private void Reset()
        {
            CustNameTb.Text = "";
            CustAddressTb.Text = "";
            CustPhoneTb.Text = "";
            CustGenderCb.SelectedIndex = 0;

        }
        private void bunifuThinButton21_Click(object sender, EventArgs e)
        {
            if (CustNameTb.Text == "" || CustAddressTb.Text == "" || CustPhoneTb.Text == "" || CustGenderCb.SelectedIndex == -1)
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("insert into CustomerTbl(CustomerName,CustomerAddress,CustomerPhone,CustomerDOB,CustomerGender)values(@CN,@CA,@CP,@CD,@CG)", conn);
                    cmd.Parameters.AddWithValue("@CN", CustNameTb.Text);
                    cmd.Parameters.AddWithValue("@CA", CustAddressTb.Text);
                    cmd.Parameters.AddWithValue("@CP", CustPhoneTb.Text);
                    cmd.Parameters.AddWithValue("@CD", CustDOB.Value.Date);
                    cmd.Parameters.AddWithValue("@CG", CustGenderCb.SelectedItem.ToString());
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Customer Added Successfully");



                    conn.Close();
                    ShowCust();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }
        int key = 0;
        private void CustomerDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

            CustNameTb.Text = CustomerDGV.SelectedRows[0].Cells[1].Value.ToString();
            CustPhoneTb.Text = CustomerDGV.SelectedRows[0].Cells[2].Value.ToString();
            CustAddressTb.Text = CustomerDGV.SelectedRows[0].Cells[3].Value.ToString();
            CustDOB.Text = CustomerDGV.SelectedRows[0].Cells[4].Value.ToString();
            CustGenderCb.SelectedItem = CustomerDGV.SelectedRows[0].Cells[5].Value.ToString();

            if (CustNameTb.Text == "")
            {
                key = 0;

            }
            else
            {
                key = Convert.ToInt32(CustomerDGV.SelectedRows[0].Cells[0].Value.ToString());
            }
        }

        private void bunifuThinButton23_Click(object sender, EventArgs e)
        {
            if (key == 0)
            {
                MessageBox.Show("Select the Customer!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Delete from CustomerTbl where CustomerNum=@Ckey", conn);
                    cmd.Parameters.AddWithValue("@Ckey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Customer Remove Successfully");


                    conn.Close();
                    ShowCust();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void bunifuThinButton22_Click(object sender, EventArgs e)
        {
            if (CustNameTb.Text == "" || CustAddressTb.Text == "" || CustPhoneTb.Text == "" || CustGenderCb.SelectedIndex == -1)
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Update  CustomerTbl Set CustomerName=@CN,CustomerAddress=@CA,CustomerPhone=@CP,CustomerDOB=@CD,CustomerGender=@CG where CustomerNum=@Ckey", conn);
                    cmd.Parameters.AddWithValue("@CN", CustNameTb.Text);
                    cmd.Parameters.AddWithValue("@CA", CustAddressTb.Text);
                    cmd.Parameters.AddWithValue("@CP", CustPhoneTb.Text);
                    cmd.Parameters.AddWithValue("@CD", CustDOB.Value.Date);
                    cmd.Parameters.AddWithValue("@CG", CustGenderCb.SelectedItem.ToString());
                    cmd.Parameters.AddWithValue("@Ckey",key);

                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Customer Record Updated Successfully");



                    conn.Close();
                    ShowCust();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void Customer_Load(object sender, EventArgs e)
        {

        }

        private void label20_Click(object sender, EventArgs e)
        {
            Login loginForm = new Login();
            loginForm.Show();
            this.Close();
        }

        private void label10_Click_1(object sender, EventArgs e)
        {
         Manufacturer obj = new Manufacturer();
            obj.Show();
            this.Hide();
        }

        private void label16_Click(object sender, EventArgs e)
        {
            Medicines obj = new Medicines();
            obj.Show();
            this.Hide();
        }

        private void label18_Click(object sender, EventArgs e)
        {
            Sellers obj = new Sellers();
            obj.Show();
            this.Hide();
        }

        private void label19_Click(object sender, EventArgs e)
        {
            Sellings obj = new Sellings();
            obj.Show();
            this.Hide();
        }

        private void CustNameTb_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsLetter(e.KeyChar) && e.KeyChar != (char)Keys.Back && e.KeyChar != (char)Keys.Space)
            {
                e.Handled = true;
                MessageBox.Show("Please Enter Alphabets Only!!.");

            }
        }

        private void CustPhoneTb_TextChanged(object sender, EventArgs e)
        {

        }

        private void CustPhoneTb_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
                MessageBox.Show("Please Numbers  Only!..");

            }
        }
    }
}
