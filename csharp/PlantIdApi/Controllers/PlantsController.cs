using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using PlantIdApi.Models;

namespace PlantIdApi.Controllers
{
    [Route("api/plants")]
    [ApiController]
    public class PlantsController : ControllerBase
    {
        private readonly ILogger<PlantsController> _logger;

        public PlantsController(ILogger<PlantsController> logger)
        {
            _logger = logger;
        }

        [HttpPost("identify")]
        public async Task<string> Identify(IFormFile files)
        {
            if (files.Length > 0)
            {
                return "Uploaded: " + files.FileName;
            }
            else
            {
                return "No file uploaded";
            }
        }
    }
}