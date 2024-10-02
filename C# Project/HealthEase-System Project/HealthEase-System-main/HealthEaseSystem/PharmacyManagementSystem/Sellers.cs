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
    public partial class Sellers : Form
    {
        public Sellers()
        {
            InitializeComponent();
            ShowSeller();
        }

        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");
        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void ShowSeller()
        {
            conn.Open();
            string query = "Select * from SellerTbl";
            SqlDataAdapter sda = new SqlDataAdapter(query, conn);
            SqlCommandBuilder Builder = new SqlCommandBuilder(sda);
            var ds = new DataSet();
            sda.Fill(ds);
            SellersDGV.DataSource = ds.Tables[0];


            conn.Close();
        }
        private void Sellers_Load(object sender, EventArgs e)
        {

        }

        private void Reset()
        {
            SNameTb.Text = "";
            SPhoneTb.Text = "";
            SAddressTb.Text = "";
            SPasswordTb.Text = "";
            SGenderCb.SelectedIndex = 0;
            key = 0;
        }
        private void SaveBtn_Click(object sender, EventArgs e)
        {
            if (SNameTb.Text == "" || SPhoneTb.Text == "" ||  SAddressTb.Text == "" || SGenderCb.SelectedIndex == -1 || SPasswordTb.Text == "" )
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("insert into SellerTbl(SellerName,SellerDOB,SellerPhone, SellerAddress,SellerGender,SellerPassword)values(@SN,@SD,@SP,@SA,@SG,@SPA)", conn);
                    cmd.Parameters.AddWithValue("@SN", SNameTb.Text);
                    cmd.Parameters.AddWithValue("@SD", SDOB.Value.Date);
                    cmd.Parameters.AddWithValue("@SP", SPhoneTb.Text);
                    cmd.Parameters.AddWithValue("@SA", SAddressTb.Text);
                    cmd.Parameters.AddWithValue("@SG", SGenderCb.SelectedItem.ToString());
                    cmd.Parameters.AddWithValue("@SPA", SPasswordTb.Text);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Seller Added Successfully");



                    conn.Close();
                    ShowSeller();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        int key = 0;
        private void SellersDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

            SNameTb.Text = SellersDGV.SelectedRows[0].Cells[1].Value.ToString();
            SDOB.Text = SellersDGV.SelectedRows[0].Cells[2].Value.ToString();
            SPhoneTb.Text = SellersDGV.SelectedRows[0].Cells[3].Value.ToString();
            SAddressTb.Text = SellersDGV.SelectedRows[0].Cells[4].Value.ToString();
            SGenderCb.SelectedItem = SellersDGV.SelectedRows[0].Cells[5].Value.ToString();
            SPasswordTb.Text = SellersDGV.SelectedRows[0].Cells[6].Value.ToString();


            if (SNameTb.Text == "")
            {
                key = 0;

            }
            else
            {
                key = Convert.ToInt32(SellersDGV.SelectedRows[0].Cells[0].Value.ToString());
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (key == 0)
            {
                MessageBox.Show("Select the Seller!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Delete from SellerTbl where SellerNum=@Skey", conn);
                    cmd.Parameters.AddWithValue("@Skey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Seller Remove Successfully");


                    conn.Close();
                    ShowSeller();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void EditBtn_Click(object sender, EventArgs e)
        {
            if (SNameTb.Text == "" || SPhoneTb.Text == "" || SAddressTb.Text == "" || SGenderCb.SelectedIndex == -1 || SPasswordTb.Text == "")
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Update  SellerTbl Set SellerName=@SN,SellerDOB=@SD,SellerPhone=@SP, SellerAddress=@SA,SellerGender=@SG,SellerPassword=@SPA where SellerNum=@Skey", conn);
                    cmd.Parameters.AddWithValue("@SN", SNameTb.Text);
                    cmd.Parameters.AddWithValue("@SD", SDOB.Value.Date);
                    cmd.Parameters.AddWithValue("@SP", SPhoneTb.Text);
                    cmd.Parameters.AddWithValue("@SA", SAddressTb.Text);
                    cmd.Parameters.AddWithValue("@SG", SGenderCb.SelectedItem.ToString());
                    cmd.Parameters.AddWithValue("@SPA", SPasswordTb.Text);
                    cmd.Parameters.AddWithValue("@Skey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Seller Record Updated Successfully");



                    conn.Close();
                    ShowSeller();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void label20_Click(object sender, EventArgs e)
        {
            Login loginForm = new Login();
            loginForm.Show();
            this.Close();
        }

        private void label10_Click_1(object sender, EventArgs e)
        {
            Dashboard obj = new Dashboard();
            obj.Show();
            this.Hide();
        }

        private void label17_Click(object sender, EventArgs e)
        {
            Customer customer = new Customer();
            customer.Show();
            this.Hide();
        }

        private void label18_Click(object sender, EventArgs e)
        {
            Sellers sellers = new Sellers();
            sellers.Show();
            this.Hide();
        }

        private void label19_Click(object sender, EventArgs e)
        {
            Manufacturer manufacturer = new Manufacturer();
            manufacturer.Show(); 
            this.Hide();
        }

        private void label16_Click(object sender, EventArgs e)
        {
            Medicines objmed = new Medicines();
            objmed.Show();
            this.Hide();
        }

        private void SNameTb_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsLetter(e.KeyChar) && e.KeyChar != (char)Keys.Back && e.KeyChar != (char)Keys.Space)
            {
                e.Handled = true;
                MessageBox.Show("Please enter Alphabets only.");

            }
        }

        private void SPhoneTb_KeyPress(object sender, KeyPressEventArgs e)
        {
            if(!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
                MessageBox.Show("Please enter numbers only.");

            }
        }
    }
}
