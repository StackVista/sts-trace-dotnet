using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text;
using StatsdClient;

namespace Datadog.RuntimeMetrics
{
    public class StatsdMetricsSubscriber : IObserver<IEnumerable<MetricValue>>, IDisposable
    {
        private readonly IStatsdUDP _statsdUdp;
        private readonly double? _sampleRate;
        private readonly string[]? _tags;

        public StatsdMetricsSubscriber(IStatsdUDP statsd, string[]? tags, double? sampleRate)
        {
            _statsdUdp = statsd ?? throw new ArgumentNullException(nameof(statsd));
            _tags = tags;
            _sampleRate = sampleRate;
        }

        public void OnCompleted()
        {
            (_statsdUdp as IDisposable)?.Dispose();
        }

        public void OnError(Exception error)
        {
        }

        public void OnNext(IEnumerable<MetricValue> payloads)
        {
            var commandBuilder = new StringBuilder();

            foreach (MetricValue payload in payloads)
            {
                commandBuilder.AppendFormat(CultureInfo.InvariantCulture, "{0}:{1}|{2}", payload.Metric.Name, payload.Value, payload.Metric.Type);

                if (_sampleRate != null)
                {
                    commandBuilder.AppendFormat(CultureInfo.InvariantCulture, "|@{0}", _sampleRate);
                }

                if (_tags?.Length > 0)
                {
                    string joinedTags = string.Join(",", _tags);
                    commandBuilder.AppendFormat(CultureInfo.InvariantCulture, "|#{0}", joinedTags);
                }

                commandBuilder.AppendLine();
            }

            //_statsdUdp.SendAsync(commandBuilder.ToString());
        }

        public void Dispose()
        {
            (_statsdUdp as IDisposable)?.Dispose();
        }
    }
}
