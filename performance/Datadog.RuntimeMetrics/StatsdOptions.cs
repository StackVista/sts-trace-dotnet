// ReSharper disable InconsistentNaming

namespace Datadog.RuntimeMetrics
{
    public class StatsdOptions
    {
        public string DD_AGENT_HOST { get; set; } = "localhost";

        public int DD_DOGSTATSD_PORT { get; set; } = 8125;
    }
}
