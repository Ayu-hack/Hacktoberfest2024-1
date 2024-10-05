using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace PharmacyManagementSystem
{
    public partial class Manufacturer : Form
    {
        public Manufacturer()
        {
            InitializeComponent();
            ShowManfac();
        }
SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");
        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void ShowManfac()
        {
            conn.Open();
            string query = "Select * from ManufacturerTbl";
            SqlDataAdapter sda = new SqlDataAdapter(query, conn);
            SqlCommandBuilder  Builder = new SqlCommandBuilder(sda);
            var ds = new DataSet();
            sda.Fill(ds);
            ManufacturerDGV.DataSource = ds.Tables[0];


            conn.Close();
        }
        private void SaveBtn_Click(object sender, EventArgs e)
        {
            if(ManfacAddressTbl.Text == "" || ManfacNameTbl.Text == "" || ManfacPhoneTbl.Text == "")
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("insert into ManufacturerTbl(ManfacName,ManfacAddress,ManfacPhone,ManfacJDate)values(@MN,@MA,@MP,@MJD)",conn);
                    cmd.Parameters.AddWithValue("@MN", ManfacNameTbl.Text);
                    cmd.Parameters.AddWithValue("@MA", ManfacAddressTbl.Text);
                    cmd.Parameters.AddWithValue("@MP", ManfacPhoneTbl.Text);
                    cmd.Parameters.AddWithValue("@MJD", ManfacJDateTbl.Value.Date);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Manfacturer Added Successfully");
                    


                    conn.Close();
                    ShowManfac();
                    Reset();

                }
                catch(Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        int key = 0;
        private void ManufacturerDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            ManfacNameTbl.Text = ManufacturerDGV.SelectedRows[0].Cells[1].Value.ToString();
            ManfacAddressTbl.Text = ManufacturerDGV.SelectedRows[0].Cells[2].Value.ToString();
            ManfacPhoneTbl.Text = ManufacturerDGV.SelectedRows[0].Cells[3].Value.ToString();
            ManfacJDateTbl.Text = ManufacturerDGV.SelectedRows[0].Cells[4].Value.ToString();

            if(ManfacNameTbl.Text == "")
            {
                key = 0;

            }
            else
            {
                key = Convert.ToInt32(ManufacturerDGV.SelectedRows[0].Cells[0].Value.ToString());
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (key ==0)
            {
                MessageBox.Show("Select the Manufacturer!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Delete from ManufacturerTbl where ManfacId=@Mkey", conn);
                    cmd.Parameters.AddWithValue("@Mkey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Manfacturer Remove Successfully");


                    conn.Close();
                    ShowManfac();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }
        private void Reset()
        {
            ManfacNameTbl.Text = "";
            ManfacAddressTbl.Text = "";
            ManfacPhoneTbl.Text = "";
            key = 0;


        }
        private void EditBtn_Click(object sender, EventArgs e)
        {
            if (ManfacAddressTbl.Text == "" || ManfacNameTbl.Text == "" || ManfacPhoneTbl.Text == "")
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Update ManufacturerTbl Set ManfacName=@MN,ManfacAddress=@MA,ManfacPhone=@MP,ManfacJDate=@MJD where ManfacId=@Mkey", conn);
                    cmd.Parameters.AddWithValue("@MN", ManfacNameTbl.Text);
                    cmd.Parameters.AddWithValue("@MA", ManfacAddressTbl.Text);
                    cmd.Parameters.AddWithValue("@MP", ManfacPhoneTbl.Text);
                    cmd.Parameters.AddWithValue("@MJD", ManfacJDateTbl.Value.Date);
                    cmd.Parameters.AddWithValue("@Mkey", key);

                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Manfacturer Recorded Updated  Successfully");


                    conn.Close();
                    ShowManfac();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void Manufacturer_Load(object sender, EventArgs e)
        {

        }

        private void panel6_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label16_Click(object sender, EventArgs e)
        {
            Medicines obj = new Medicines();
            obj.Show();
            this.Hide();
        }

        private void label17_Click(object sender, EventArgs e)
        {
            Customer obj = new Customer();
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

        private void label20_Click(object sender, EventArgs e)
        {
            Login loginForm = new Login();
            loginForm.Show();
            this.Close();
        }

        private void ManfacNameTbl_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsLetter(e.KeyChar) && e.KeyChar != (char)Keys.Back && e.KeyChar != (char)Keys.Space)
            {
                e.Handled = true;
                MessageBox.Show("Please enter Alphabets only.");

            }
        }

        private void ManfacPhoneTbl_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
                MessageBox.Show("Please enter numbers only.");

            }
        }
    }
}
