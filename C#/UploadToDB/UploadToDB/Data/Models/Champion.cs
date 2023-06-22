using System.ComponentModel.DataAnnotations;

namespace UploadToDB.Data.Models
{
    public class Champion
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string Name { get; set; } = null!;

        [Required]
        public string ImageURL { get; set; } = null!;
    }
}
